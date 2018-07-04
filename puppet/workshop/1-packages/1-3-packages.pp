
node 'vagrant.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}

	exec { 'apt-update':                  
		command => '/usr/bin/apt-get update'
	}

	Package { 
		ensure => 'installed' 
	}

	package { 'gcc-multilib': }
	package { 'g++': }
}

