node 'default' {}
file { "/var/tmp/testfile":
        ensure => "present",
        owner => "root",
        group => "root",
        mode => "664",
	#content => "This is a test file created using puppet.  Puppet is really cool",
	content => "This is a New content required",
}

node "vagrant.auranetworks.in"
{
	file { "/var/tmp/test2":
		ensure => "directory",
		owner => "root",
		group => "root",
		mode => "777",
	}
}
