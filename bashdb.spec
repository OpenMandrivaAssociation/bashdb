%define oversion 4.2-0.8

Name:		bashdb
Summary:	BASH debugger, the BASH symbolic debugger
Group:		Development/Other
Version:	4.2_0.8
Release:	3
License:	GPLv2+
Url:		http://bashdb.sourceforge.net/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{oversion}.tar.bz2
BuildRequires:	bash
Requires:	bash

%description
The Bash Debugger Project is a source-code debugger for bash,
which follows the gdb command syntax.
The purpose of the BASH debugger is to check
what is going on “inside” a bash script, while it executes:
    * Start a script, specifying conditions that might affect its behavior.
    * Stop a script at certain conditions (break points).
    * Examine the state of a script.
    * Experiment, by changing variable values on the fly.
The 4.0 series is a complete rewrite of the previous series.
Bashdb can be used with ddd: ddd --debugger %{_bindir}/%{name} <script-name>.

%files
%doc doc/*.html AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info.*

%prep
%setup -q -n %{name}-%{oversion}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%changelog
* Sat Jun 02 2012 Andrey Bondrov <abondrov@mandriva.org> 4.2_0.8-3
+ Revision: 801970
- Drop some legacy junk

* Sun Dec 11 2011 Zé <ze@mandriva.org> 4.2_0.8-2
+ Revision: 740290
- use macros
- fix scriptlets
- change to preun

* Sat Dec 10 2011 Zé <ze@mandriva.org> 4.2_0.8-1
+ Revision: 740136
- imported package bashdb


* Sat Dec 10 2011 Zé <ze@mandriva.org> 4.2_0.8-1.mde
- first packaget package
