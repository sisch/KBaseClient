#!/usr/bin/env perl
########################################################################
# Authors: Christopher Henry, Scott Devoid, Paul Frybarger
# Contact email: chenry@mcs.anl.gov
# Development location: Mathematics and Computer Science Division, Argonne National Lab
########################################################################
use strict;
use warnings;
use Getopt::Long::Descriptive;
use Text::Table;
use Bio::KBase::workspace::ScriptHelpers qw(get_ws_client parseWorkspaceInfo);

my $serv = get_ws_client();
#Defining globals describing behavior
my $primaryArgs = ["Workspace ID"];
my $servercommand = "create_workspace";
my $translation = {
	"Workspace ID" => "workspace",
};
#Defining usage and options
my ($opt, $usage) = describe_options(
    'kb_createws <'.join("> <",@{$primaryArgs}).'> %o',
    [ 'description|d=s', 'Workspace description (1000 characters max)',{"default"=>''}],
    [ 'globalread|g=s', 'Set global read permissions (r=read,n=none)',{"default"=>'n'}],
    [ 'showerror|e', 'Show any errors in execution',{"default"=>0}],
    [ 'verbose|v', 'Print verbose messages' ],
    [ 'help|h|?', 'Print this usage information' ],
);
if (defined($opt->{help})) {
	print $usage;
	exit 0;
}
#Processing primary arguments
foreach my $arg (@{$primaryArgs}) {
	$opt->{$arg} = shift @ARGV;
	if (!defined($opt->{$arg})) {
		print $usage;
		exit 0;
	}
}
#Instantiating parameters
my $params = { };
foreach my $key (keys(%{$translation})) {
	if (defined($opt->{$key})) {
		$params->{$translation->{$key}} = $opt->{$key};
	}
}
if (defined($opt->{description})) {
	$params->{"description"} = $opt->{description};
}
if (defined($opt->{globalread})) {
	$params->{"globalread"} = $opt->{globalread};
}

#Calling the server
my $output;
if ($opt->{showerror} == 0){
	eval { $output = $serv->$servercommand($params); };
	if($@) {
		print "Workspace creation failed! Run with -e for full stack trace.\n";
		print STDERR $@->{message}."\n";
		if(defined($@->{status_line})) {print STDERR $@->{status_line}."\n" };
		print STDERR "\n";
		exit 1;
	}
} else{
    $output = $serv->$servercommand($params);
}

my $obj = parseWorkspaceInfo($output);
print "Workspace created with name: ".$obj->{workspace}." and id: ".$obj->{id}."\n";

exit 0;