%global debug_package   %{nil}
%global import_path     github.com/stretchr/objx
%global commit          cbeaeb16a013161a98496fad62933b1d21786672
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-stretchr-objx
Version:        0
Release:        0.2.git%{shortcommit}%{?dist}
Summary:        Go package for dealing with maps, slices, JSON and other data
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/objx-%{shortcommit}.tar.gz
BuildArch:      noarch

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
%setup -q -n objx-%{commit}

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
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/codegen
%{gopath}/src/%{import_path}/*
%{gopath}/src/%{import_path}/codegen/*

%changelog
* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.gitcbeaeb1
- do not redefine gopath

* Wed Aug 06 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.gitcbeaeb1
- First package for Fedora.
