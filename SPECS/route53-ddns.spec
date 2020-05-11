%define debug_package %{nil}

%global gh_user jc21

Name:           route53-ddns
Version:        1.0.4
Release:        1%{?dist}
Summary:        A command to detect your public IP and update a route53 A record when changed
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Sick of using Dynamic DNS services that are costly or annoying?
Already use Route53 for your domain DNS?
Do you have a dynamically assigned IP address?
This is the command for you.

%prep
%setup -qn %{name}-%{version}

%build
go build -o bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon May 11 2020 Jamie Curnow <jc@jc21.com> 1.0.4-1
- v1.0.4

* Fri Jul 26 2019 Jamie Curnow <jc@jc21.com> 1.0.3-1
- v1.0.3

* Thu Jul 25 2019 Jamie Curnow <jc@jc21.com> 1.0.2-1
- v1.0.2

* Thu Jul 25 2019 Jamie Curnow <jc@jc21.com> 1.0.1-1
- v1.0.1

* Thu Jul 25 2019 Jamie Curnow <jc@jc21.com> 1.0.0-1
- Initial Spec

