# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/conferences/sugconf
# catalog-date 2008-04-16 11:52:05 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-sugconf
Version:	20080416
Release:	4
Summary:	SAS(R) user group conference proceedings document class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/sugconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class may be used to typeset articles to be published in
the proceedings of SAS(R) User group conferences and workshops.
The layout produced by the class is based on that published by
SAS Institute (2006).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sugconf/sugconf.cls
%doc %{_texmfdistdir}/doc/latex/sugconf/README
%doc %{_texmfdistdir}/doc/latex/sugconf/SUGI-paper-example.txt
%doc %{_texmfdistdir}/doc/latex/sugconf/article-example.bat
%doc %{_texmfdistdir}/doc/latex/sugconf/article-example.pdf
%doc %{_texmfdistdir}/doc/latex/sugconf/article-example.tex
%doc %{_texmfdistdir}/doc/latex/sugconf/sugconf-example.bat
%doc %{_texmfdistdir}/doc/latex/sugconf/sugconf-example.pdf
%doc %{_texmfdistdir}/doc/latex/sugconf/sugconf-example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080416-2
+ Revision: 756353
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080416-1
+ Revision: 719612
- texlive-sugconf
- texlive-sugconf
- texlive-sugconf
- texlive-sugconf

