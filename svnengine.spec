Summary:	Subversion helper for CFengine
Name:		svnengine
Version:	0.4
Release:	%mkrel 1
License:	GPL
Group:		Development/Python
URL:		http://pulseaudio.revolutionlinux.com/Svnengine
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	python-pysvn >= 1.5.1
Requires:	python-%{name} >= %{version}
BuildRequires:	python-devel

%description
As the name suggests, Svnengine purpose is to make integration between SVN and
Cfengine easy. While working with Cfengine, there are many steps that are
repetitive, boring and error prone. With Svnengine, the system administrator
can create cfengine class in a more automated manner.

The principle of operation is simple. Files and attributes of files are stored
in svn repository. If a file is added with svnengine, properties will be set
for mode, owner, etc. Each files added into a directory can be used to generate
the cfengine class file automaticaly. This file can be added to the cfengine
server, and apply files to servers.

It's also useful for testing. For example, you can apply a class even without
a cfengine server. Also, you can change configuration files directly on the
filesystem and gather changes by using the collect feature, and then commit.

Bet you will love it! 

%package -n	python-%{name}
Summary:	Subversion helper for CFengine
Group:		Development/Python

%description -n	python-%{name}
As the name suggests, Svnengine purpose is to make integration between SVN and
Cfengine easy. While working with Cfengine, there are many steps that are
repetitive, boring and error prone. With Svnengine, the system administrator
can create cfengine class in a more automated manner.

The principle of operation is simple. Files and attributes of files are stored
in svn repository. If a file is added with svnengine, properties will be set
for mode, owner, etc. Each files added into a directory can be used to generate
the cfengine class file automaticaly. This file can be added to the cfengine
server, and apply files to servers.

It's also useful for testing. For example, you can apply a class even without
a cfengine server. Also, you can change configuration files directly on the
filesystem and gather changes by using the collect feature, and then commit.

Bet you will love it! 

%prep



%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}

%files -n python-%{name} -f INSTALLED_FILES
%defattr(-,root,root)
%exclude %{_bindir}/%{name}


