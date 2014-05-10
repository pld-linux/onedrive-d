Summary:	Microsoft OneDrive daemon on Ubuntu
Name:		onedrive-d
Version:	0.7.0
Release:	0.1
License:	LGPL v3
Group:		Daemons
Source0:	https://github.com/xybu92/onedrive-d/archive/v%{version}-alpha/%{name}-%{version}-alpha.tar.gz
# Source0-md5:	2ab5ae73df9e04da7247afd9c4fd30ca
URL:		http://xybu.me/projects/onedrive-d/
Requires:	python-onedrive
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
onedrive-d project intends to develop an OneDrive (formerly SkyDrive)
daemon on (X)Ubuntu Linux. The program is mainly written in Python and
supplemented by Bash shell scripts.

%prep
%setup -q -n %{name}-%{version}-alpha

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md WIP.md
%attr(755,root,root) %{_bindir}/onedrive-daemon
%attr(755,root,root) %{_bindir}/onedrive-utils
%{py_sitescriptdir}/onedrive
%{py_sitescriptdir}/onedrive_d-0.7-py*.egg-info
