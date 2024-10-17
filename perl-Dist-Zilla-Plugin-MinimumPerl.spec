%define upstream_name    Dist-Zilla-Plugin-MinimumPerl
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Detects the minimum version of Perl required for your dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Perl::MinimumVersion)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This plugin uses the Perl::MinimumVersion manpage to automatically find the
minimum version of Perl required for your dist and adds it to the prereqs.
You can specify a version of Perl to override the scanning logic.

	# In your dist.ini:
	[MinimumPerl]

This plugin accepts the following options:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

