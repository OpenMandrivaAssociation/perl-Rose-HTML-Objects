%define upstream_name	 Rose-HTML-Objects
%define upstream_version 0.618
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.618
Release:	1

Summary:	Object-oriented interfaces for HTML
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Rose/Rose-HTML-Objects-0.618.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
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

%changelog
* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.611.0-1mdv2011.0
+ Revision: 602388
- update to new version 0.611

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2011.0
+ Revision: 596640
- update to 0.610

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.607.0-1mdv2011.0
+ Revision: 552624
- update to 0.607

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.606.100-1mdv2010.1
+ Revision: 468887
- update to 0.6061

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.606.0-1mdv2010.1
+ Revision: 466752
- update to 0.606

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.605.0-1mdv2010.1
+ Revision: 461351
- update to 0.605

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.604.0-1mdv2010.0
+ Revision: 442653
- update to 0.604

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.603-1mdv2010.0
+ Revision: 374377
- update to new version 0.603

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.602-1mdv2010.0
+ Revision: 372530
- update to 0.602
- update source

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.555-1mdv2009.1
+ Revision: 296797
- update to new version 0.555

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.554-1mdv2009.0
+ Revision: 218716
- update to new version 0.554

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.553-1mdv2008.1
+ Revision: 178279
- update to new version 0.553

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.552-1mdv2008.1
+ Revision: 135952
- update to new version 0.552

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.550-1mdv2008.1
+ Revision: 106643
- new version

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 0.549-1mdv2008.0
+ Revision: 60696
- New version 0.549


* Wed Jun 14 2006 Scott Karns <scottk@mandriva.org> 0.53-1mdv2007.0
- Version 0.53

* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 0.52-1mdk
- Initial MDV package


