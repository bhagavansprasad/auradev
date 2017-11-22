#!/usr/bin/perl -w
###############################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
# the GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
###############################################################################

###############################################################################
# Author: Robby Garrison, Vulcan Technologies
#         robby@vulcantechnologies.com
#	  
# Description:
#   Parses the Dan's Guardian access.log file for *DENIED* entries,
#   and outputs them to HTML.  Also rotates it's own output files, and
#   uses much cheapness to try to keep the access.log file rotated
#   too.
#
# To Use:
#   Change the "$log_file" and "$parser_output_dir" variables to match
#   your setup.  To run, simply execute './dg-log-parser-0.03.pl' (you may
#   need to 'chmod +x dg-log-parser-0.03.pl') and then
#   cd to the  "$parser_output_dir" and use a web browser to open the 
#   *.html file with the appropriate date name, and view your log output
#   *NOTE*  this log-parser only outputs log entries where access to a 
#   page has been denied (since these are the only entries of interest to
#   me 8-), but you can change this behavior by modifying the regex under
#   "#Begin parsing of log data".
###############################################################################

use File::Copy;

# Open log file for reading
$log_file = '/var/log/dansguardian/access.log';
$parser_output_dir = '/var/log/dansguardian/html';

# Make sure that the output directory for the parser *.html files exists & create if it doesn't
unless (-e $parser_output_dir && -d $parser_output_dir) {
    mkdir ("$parser_output_dir");
}

open( LOG_FILE, "<", "$log_file" )
    or die "No log file exists.  Is Dan's Guardian even running?\n $! \n";

# Read current time...
($null,$minute,$hour,$day,$month,$year,$null,$null,$null)=localtime(time);

# ...and adjust as necessary
if ($hour < 12) {
    $ampm = "am";
} else {
    $ampm = "pm";
}
if ($hour == 12) {
    $hour=$hour;
} elsif ($hour == 0) {
    $hour = $hour + 12;
} elsif ($hour > 12) {
    $hour = $hour - 12;
}
if ($minute < 10) {
    $minute = "0$minute";
}
$year = $year + 1900;

$month = $month + 1;
@months = qw(January February March April May June July August September October November December);
$written_month = $months[$month - 1];

# Open 'log.html' for writing, and select it to send output to
$html=("$parser_output_dir/$written_month-$day-$year.html");
open( HTML, ">", "$html" );
select HTML;

# Print html-header
print "<html><head><title>Dan\'s Guardian Log-Parser $written_month $day\, $year $hour\:$minute$ampm </title>\n";
print "</head><body bgcolor=\"b5d8ab\"><h2>Dan\'s Guardian Log<h2/><h3>Log Date\: $written_month $day\, $year $hour\:$minute$ampm </h3>\n";
print "<br><table border=\"1\" bgcolor=\"7f7f7f\">\n";
print "<tr bgcolor=000ea8><td><font color=#ffffff size=+1><b>Date</b></font></td>\n";
print "<td><font color=#ffffff size=+1><b>PC Address</b></font></td>\n";

# Uncomment the following line, the two other appropriate lines further down,
# and the "get_hostname" subroutine to add hostname resolution to the log output file.
# Each of your clients must have entries in your local "/etc/hosts" file, or your DNS server.
# **WARNING** Turning on this option greatly increases the time it takes to generate
# the log ouput file.

#print "<td><font color=#ffffff size=+1><b>PC Name</b></font></td>\n";
print "<td><font color=#ffffff size=+1><b>URL</b></font></td>\n";
print "<td><font color=#ffffff size=+1><b>Reason for Denial<b></font></td></tr>\n";

# init variable used to alternate row color
$tr_alternate = 0;

# Begin parsing of log data
foreach $logfile_line (<LOG_FILE>) {
    $logfile_line =~ s/GET//;
    if ($logfile_line =~ m/\*DENIED\*/) {
	$tr_alternate = $tr_alternate + 1;
	@logfile_fields = split /\s+/, $logfile_line, 6;
	$date = ($logfile_fields[0]);
	$time = ($logfile_fields[1]);
	$client_ip = ($logfile_fields[2]);
	$url = ($logfile_fields[3]);
	$reason = ($logfile_fields[5]);
	@hit_date = split /\./, $date, 3;
	$hit_year = ($hit_date[0]); $hit_month = ($hit_date[1]); $hit_day = ($hit_date[2]);

	# Uncomment the following for hostname resolution
	#&get_hostname();
	if ($tr_alternate == 1) {
	    print "<tr bgcolor=b7b7b7>";
	    $tr_alternate = $tr_alternate - 2;
	}

	print "<td>$hit_month\/$hit_day\/$hit_year $time</td>\n";
	print "<td>$client_ip</td>\n";

	# Uncomment the following for hostname resolution
	#print "<td>$pc_name</td>";
	print "<td>$url</td>\n";
	print "<td>$reason</td></tr>\n";
    }
}

# Nice little "footer" thingy
print "</table>\n";
print "<br><br><hr><br></b><h5>Courtesy of the \"Dan\'s Guardian Log Analyzer\" by Robby Garrison of Vulcan Technologies, 2002</h5></body></html>\n";

# Return the '*.html' file to the state we found it ....err, sorta.
select STDOUT;

# Check to see if "access.log" needs rotating, and do so if it does
if (-M $log_file > 0.98) {
    move ("$log_file", "$log_file.$month.$day.$year");
}

# Groom directory of files older than 14 days if more than 14 files exist
@dir_contents = glob ("$parser_output_dir");
$num_files = @dir_contents;
if ($num_files > 14) {
    foreach $file (@dir_contents) {
	if (-M $file > 14) {
	    unlink("$file");
	}
    }
}

# Get a client computer's name
#sub get_hostname
#{
#	use Socket;
#	$ipaddr = inet_aton("$client_ip");
#	$pc_name = gethostbyaddr ($ipaddr, AF_INET);
#}

