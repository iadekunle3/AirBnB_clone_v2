# Install Nginx
class { 'nginx': }

# Create necessary directories
file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure => 'file',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0644',
  content => '<html><body>Holberton School</body></html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test/'],
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80;
                listen [::]:80;
                location /hbnb_static/ {
                    alias /data/web_static/current/;
                }
            }",
  notify => Service['nginx'],
}

# Set ownership of /data/ folder recursively
exec { 'set_ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'test "$(stat -c %U:%G /data/)" != "ubuntu:ubuntu"',
}
