# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/conferences/sugconf
# catalog-date 2008-04-16 11:52:05 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-sugconf
Version:	20080416
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class may be used to typeset articles to be published in
the proceedings of SAS(R) User group conferences and workshops.
The layout produced by the class is based on that published by
SAS Institute (2006).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
