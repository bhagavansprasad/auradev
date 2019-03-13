
exec { 'apt-update':                  
	command => '/usr/bin/apt-get update'
}

node 'vagrant.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}

	Package { 
  		require => Exec['apt-update'], 
		ensure => 'installed' 
	}

	package { 'gcc-multilib': }
	package { 'g++': }
}

