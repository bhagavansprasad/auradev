#!/usr/bin/perl
use strict;
use warnings;
use Text::CSV;
use Expect;
use Switch;

my ($name, $fullname, $uid, $gid, $phone, $address, $enabled, $homedir, $shell,
$home_phone, $room_number, $other, $i, $home_dir, $usersfile, $su_cmd, $csv,
@columns, $err);

print "$#ARGV\n";
if ($#ARGV+1 < 3)
{
	print "Invalid/Insufficient arguments\n";
	print "Usage: perl adduser.pl users.csv\n\n";
	exit;
}

$home_dir = "/home/bhagavan";
$usersfile = $ARGV[1];
#$home_dir/auradev/users.csv";
$su_cmd = read_linux_type_file();
$csv = Text::CSV->new();

open (CSV, "<", $usersfile) or die $!;

$i = 0;
while (<CSV>) {
	if ($csv->parse($_) && $i != 0) 
	{
		@columns = $csv->fields();
		add_user(@columns);
	}
	else
	{
		$err = $csv->error_input;
		print "Can't open file\n";
		close CSV;
		exit;
	}
	$i++;
}
close CSV;

sub add_user
{
	my ($timeout, @columns, $exp);
	$timeout = 1;
	@columns = @_;
	($name, $fullname, $uid, $gid, $phone, $address, $enabled) =
		($columns[0], $columns[1], $columns[2], $columns[3], $columns[4], $columns[5], $columns[6]);
	print "$name, $fullname, $uid, $gid, $phone, $address, $enabled\n";

	$homedir = "/home/$name";
	print "homedir :$homedir\n";

	$exp = Expect->spawn($su_cmd);

	$exp->expect($timeout,
			[ 'password' => sub { $exp->send("jnjnuh\r"); } ],
			[ 'root'     => sub { $exp->send("whoami\r"); } ]
		    );

	$exp->expect($timeout, [ 'root' => sub { $exp->send("whoami\r"); } ]);
	$exp->send("adduser $name --home $homedir --shell /bin/bash --uid $uid --gid $gid\r");

	$exp->expect($timeout,
			[ 'already' => sub { print "User is already exits\n"; $exp->send("exit\r");
				$exp->soft_close();
				return;
				}
			]
		    );

	$exp->expect($timeout, [ 'password'     => sub { $exp->send("jnjnuh\r");   } ]);
	$exp->expect($timeout, [ 'password'     => sub { $exp->send("jnjnuh\r");   } ]);
	$exp->expect($timeout, [ 'Full Name'    => sub { $exp->send("$fullname\r");   } ]);
	$exp->expect($timeout, [ 'Room Number'  => sub { $exp->send("$room_number\r"); } ]);
	$exp->expect($timeout, [ 'Work Phone'   => sub { $exp->send("$phone\r");      } ]);
	$exp->expect($timeout, [ 'Home Phone'   => sub { $exp->send("$home_phone\r"); } ]);
	$exp->expect($timeout, [ 'Other'        => sub { $exp->send("$other\r"); } ]);
	$exp->expect($timeout, [ 'correct'      => sub { $exp->send("Y\r"); } ]);
	$exp->soft_close();
	$exp->send("exit");
	return;
}

sub read_linux_type_file
{
	my ($f, @data);
	$f = "/etc/issue";

	open F, "< $f" or die "Can't open $f : $!";
	@data = <F>;

	switch ($data[0]) 
	{
		case /Ubuntu/i  { print "Ubuntu\n"; return "sudo su";}
		case /Redhat/i 	{ print "Redhat\n"; return "su";}
		case /Debian/i 	{ print "Redhat\n"; return "su";}
		else		{ print "Unknown linux flavour\n"; return "invalid";}
	}

	close F;

	return "bye";
}

sub temp
{
#print "$columns[0]:$columns[1]:$columns[2]:$columns[3]:$columns[4]:$columns[5]:$columns[6]\n";
}
