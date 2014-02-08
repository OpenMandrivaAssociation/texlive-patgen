# revision 26689
# category TLCore
# catalog-ctan /obsolete/systems/knuth/unsupported/texware/patgen.web
# catalog-date 2011-07-17 16:49:53 +0200
# catalog-license knuth
# catalog-version 2.3
Name:		texlive-patgen
Epoch:		1
Version:	2.3
Release:	2
Summary:	Generate hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/systems/knuth/unsupported/texware/patgen.web
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-patgen.bin

%description
This is the last version of the program distributed by Knuth;
it advertises itself as a pattern generator for "the algorithm
used in TeX", but, of course, the patterns used in modern
distributions are Unicode-based.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/patgen.1*
%doc %{_texmfdir}/doc/man/man1/patgen.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:2.3-1
+ Revision: 812727
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 754704
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 719204
- texlive-patgen
- texlive-patgen
- texlive-patgen
- texlive-patgen

