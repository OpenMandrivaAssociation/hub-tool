%undefine _debugsource_packages

Name:		hub-tool
Version:	0.4.6
Release:	1
Source0:	https://github.com/docker/hub-tool/archive/refs/tags/v%{version}.tar.gz
# `go mod vendor`
Source1:	vendor.tar.xz
Summary:	CLI tool for working with Docker Hub
URL:		https://github.com/docker/hub-tool
License:	Apache-2.0
Group:		Development/Tools
BuildRequires:	golang

%description
CLI tool for working with Docker Hub

%prep
%autosetup -p1 -a1

%conf

%build
go build

%install
mkdir -p %{buildroot}%{_bindir}
mv hub-tool %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/hub-tool
