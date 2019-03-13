node 'agent1' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}
}

node 'foreman.auradev.com' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}
}

node 'vagrant.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}
}

node 'docker.auranetworks.in' {
	file { '/tmp/hello':
		content => "I got it, Hello, I am Aura, with new content\n",
	}
}
