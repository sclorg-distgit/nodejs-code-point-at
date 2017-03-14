%{?scl:%scl_package nodejs-nodejs-bl}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename code-point-at
%global enable_tests 0
# tests disabled until 'ava' is packaged for Fedora

Name:		%{?scl_prefix}nodejs-code-point-at
Version:	1.0.0
Release:	3%{?dist}
Summary:	ES2015 String#codePointAt() ponyfill

License:	MIT
URL:		https://github.com/sindresorhus/code-point-at
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/code-point-at/v%{version}/test.js



ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(ava)
BuildRequires:	%{?scl_prefix}npm(number-is-nan)
%endif

%description
ES2015 String#codePointAt() ponyfill

%prep
%setup -q -n package
# setup the tests
cp -r %{SOURCE1} .


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/node test.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-3
- Add scl macros

* Mon Feb 29 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Fix test.js

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
