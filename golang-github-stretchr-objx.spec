%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         stretchr
%global repo            objx
# https://github.com/stretchr/objx
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          cbeaeb16a013161a98496fad62933b1d21786672
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        Go package for dealing with maps, slices, JSON and other data
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
Objx provides the `objx.Map` type, which is a `map[string]interface{}` that
exposes a powerful `Get` method (among others) that allows you to easily and
quickly get access to data within the map, without having to worry too much
about type assertions, missing data, default values etc. 

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Requires:       golang(github.com/stretchr/testify)
Summary:        Go package for dealing with maps, slices, JSON and other data
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Objx provides the `objx.Map` type, which is a `map[string]interface{}` that
exposes a powerful `Get` method (among others) that allows you to easily and
quickly get access to data within the map, without having to worry too much
about type assertions, missing data, default values etc. 

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}/
cp -pav codegen %{buildroot}/%{gopath}/src/%{import_path}/

%check
# as long as there is circular dependency between 
# golang-github-stretchr-testify and golang-github-stretchr-objx
# there can not by test

%files devel
%doc LICENSE.md README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitcbeaeb1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.gitcbeaeb1
- do not redefine gopath

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.gitcbeaeb1
- First package for Fedora.
