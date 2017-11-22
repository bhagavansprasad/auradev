
node 'vagrant.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}

	exec { 'apt-update':                  
		command => '/usr/bin/apt-get update'
	}

	Package { ensure => 'installed' }

 	# you can specify the packages in an array ...
  	$enhancers = [ 'g++-multilib', 'patch' ]
	package { $enhancers: }
}

