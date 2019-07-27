#!/usr/local/bin/perl

#��������������������������������������������������������������������
#�� DAY COUNTER-EX : check.cgi - 2017/05/14
#�� copyright (c) KentWeb, 1997-2017
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

# ���W���[���錾
use strict;
use CGI::Carp qw(fatalsToBrowser);

require "./init.cgi";
my %cf = set_init();

print <<EOM;
Content-type: text/html

<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<title>Check Mode</title>
</head>
<body>
<b>Check Mode: [ $cf{version} ]</b>
<ul>
EOM

# ���O�t�@�C���m�F
my %log = (
	logfile => '�݌v',
	todfile => '�{��',
	yesfile => '���',
	dayfile => '����',
	monfile => '����',
	);
	
	for ( keys %log ) {
	if (-f $cf{$_}) {
		print "<li>$log{$_}�t�@�C���p�X : OK\n";
		
		# ���O�t�@�C���̃p�[�~�b�V����
		if (-r $cf{$_} && -w $cf{$_}) {
			print "<li>$log{$_}�t�@�C���p�[�~�b�V���� : OK\n";
		} else {
			print "<li>$log{$_}�t�@�C���p�[�~�b�V���� : NG\n";
		}
	} else {
		print "<li>$log{$_}�t�@�C���p�X : NG\n";
	}
}

# �e���v���[�g
if (-f "$cf{tmpldir}/list.html") {
	print "<li>�e���v���[�g : OK\n";
} else {
	print "<li>�e���v���[�g : NG\n";
}

# �摜�`�F�b�N
for ( $cf{gifdir1}, $cf{gifdir2} ) {
	foreach my $i (0 .. 9) {
		if (-e "$_/$i.gif") {
			print "<li>�摜 : $_/$i.gif �� OK\n";
		} else {
			print "<li>�摜 : $_/$i.gif �� NG\n";
		}
	}
}

eval { require $cf{gifcat_pl}; };
if ($@) {
	print "<li>gifcat.pl�e�X�g : NG\n";
} else {
	print "<li>gifcat.pl�e�X�g : OK\n";
}

eval { require Image::Magick; };
if ($@) {
	print "<li>Image::Magick�e�X�g : NG\n";
} else {
	print "<li>Image::Magick�e�X�g : OK\n";
}

print <<EOM;
</ul>
</body>
</html>
EOM

exit;
