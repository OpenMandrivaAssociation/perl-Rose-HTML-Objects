%define upstream_name	 Rose-HTML-Objects
%define upstream_version 0.619
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Object-oriented interfaces for HTML
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Rose/Rose-HTML-Objects-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class:InsideOut)
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(Email::Valid)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Image::Size)
BuildRequires:	perl(Rose::DateTime) >= 0.0133
BuildRequires:	perl(Rose::Object) >= 0.015
BuildRequires:	perl(Rose::URI) >= 0.021
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Scalar::Defer)
BuildRequires:	perl(URI::Escape)

BuildArch:	noarch

Requires:	perl(Rose::DateTime) >= 0.0133
Requires:	perl(Rose::Object) >= 0.015
Requires:	perl(Rose::URI) >= 0.021

%description
The Rose::HTML::Object::* family of classes represent HTML tags, or
groups of tags. These objects allow HTML to be arbitrarily
manipulated, then serialized to actual HTML (or XHTML). Currently, the
process only works in one direction. Objects cannot be constructed
from their serialized representations. In practice, given the purpose
of these modules, this is not an important limitation.

Any HTML tag can theoretically be represented by a
Rose::HTML::Object-derived class, but this family of modules was
originally motivated by a desire to simplify the use of HTML forms.

The form/field object interfaces have been heavily abstracted to allow
for input and output filtering, inflation/deflation of values, and
compound fields (fields that contain other fields). The classes are
also designed to be subclassed. The creation of custom form and field
subclasses is really the "big win" for these modules.

There is also a simple image tag class which is useful for
auto-populating the width and height attributes of img tags. Future
releases may include object representations of other HTML
tags. Contributions are welcome.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/Rose

