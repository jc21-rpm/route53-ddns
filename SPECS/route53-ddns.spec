%define debug_package %{nil}

%global gh_user jc21

Name:           route53-ddns
Version:        1.0.0
Release:        1%{?dist}
Summary:        A command to detect your public IP and update a route53 A record when changed
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  git golang

%description
Sick of using Dynamic DNS services that are costly or annoying?
Already use Route53 for your domain DNS?
Do you have a dynamically assigned IP address?
This is the command for you.

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
ln -snf %{_builddir}/%{name}-%{version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
export GO111MODULE=on
go build -o %{_builddir}/bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jul 25 2019 Jamie Curnow <jc@jc21.com> 1.0.0-1
- Initial Spec

