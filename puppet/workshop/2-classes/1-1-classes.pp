class auradev_sdk {
	exec { 'apt-update':                  
		command => '/usr/bin/apt-get update'
	}

	Package { ensure => 'installed' }
  	$dev_tools = [ 'patch', 'pbzip2' ]
	package { $dev_tools: }
}

node 'vagrant.auranetworks.in' {
    include auradev_sdk
}
