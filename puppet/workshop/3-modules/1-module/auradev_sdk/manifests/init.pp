class auradev_sdk {
	exec { 'apt-update':                  
        command => '/usr/bin/apt-get update'
	}

	#package { 'g++': }
	#package { ['gcc-multilib','g++']: }


	$languages = ['gcc', 'gcc-multilib', 'g++', 'g++-multilib']
	$tools = ['patch', 'pbzip2', 'gettext', 'libxml2-utils', 'aptitude']
	$scripts = ['gawk', 'imagemagick', 'python-simplejson', 'lib32z1', 'python-dbus', 'python-pip']
	$ver_controls = ['doxygen', 'librsvg2-bin', 'hgview', 'libxml-dumper-perl', 'mercurial', 'pigz']

    package { $languages: }
    package { $tools: }
    package { $scripts: }
    package { $ver_controls: }
}


