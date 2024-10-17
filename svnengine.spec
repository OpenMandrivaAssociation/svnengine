Summary:	Subversion helper for CFengine
Name:		svnengine
Version:	0.4
Release:	7
License:	GPL
Group:		Development/Python
URL:		https://pulseaudio.revolutionlinux.com/Svnengine
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	python-pysvn >= 1.5.1
Requires:	python-%{name} >= %{version}
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%files -n python-%{name}
%defattr(-,root,root)
%{py_puresitedir}/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.4-6mdv2011.0
+ Revision: 598175
- update file list

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2010.0
+ Revision: 445270
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.4-5mdv2009.1
+ Revision: 323374
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 261277
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.4-3mdv2009.0
+ Revision: 253793
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2007.0
+ Revision: 130398
- fix deps
- Import svnengine

* Thu Mar 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdv2007.1
- initial Mandriva package

