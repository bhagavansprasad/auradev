node 'vagrant.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}

 	package { 'gcc': ensure => installed }
}
