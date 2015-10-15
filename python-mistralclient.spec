%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%global release_name liberty

Name:           python-mistralclient
Version:        XXX
Release:        XXX
Summary:        Python client for Mistral REST API
Group:          Development/Libraries
License:        Apache License, Version 2.0
URL:            https://launchpad.net/python-mistralclient
Source0:        https://launchpad.net/%{name}/%{release_name}/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  libyaml-devel
BuildRequires:  python-pbr
BuildRequires:  python-d2to1
Requires:       python-pbr >= 1.6
Requires:       python-requests >= 2.5.2
Requires:       python-cliff >= 1.14.0
Requires:       python-keystoneclient >= 1:1.6.0
Requires:       PyYAML >= 3.1.0

%description
Sytem package - python-mistralclient
Python package - python-mistralclient

%prep
%setup -q -n python-mistralclient-%{upstream_version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{python_sitelib}/

%changelog
