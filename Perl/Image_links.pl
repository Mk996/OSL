#!/usr/bin/perl
use WWW::Mechanize;

print "Enter website url(www.xyz.com):";
$user_inp = <STDIN>;
print "Enter number of images you wanna download:";
chomp($downlim = <STDIN>);

$url = "http://$user_inp";
$count = 1;

my $mechanize = WWW::Mechanize->new(autocheck => 1);

$mechanize->get($url);

my $title = $mechanize->title;

print "$title";

my @links = $mechanize->links;

open(FH, ">links.txt");

foreach my $link (@links) {

   my $href = $link->url;

   my $name = $link->text;
   if($name eq ""){
      
   }
   else{
   print FH $name;
   print FH " --> ";
   print FH $href;
   print FH "\n";
   print FH "\n";
   
   print "label - $name \n";
   print "link - $href \n";
   }
   
}

close(FH);

#code for images

my @links = $mechanize->images;

foreach my $link (@links) {
      print $link;
      $work = "$count.jpg";
      $mechanize->get($link->url, ':content_file' => $work); 
      $size = -s $work;
      if($size < 1024){
      unlink $work;
      }
      else{
      $count = $count+1; 
      }
      if($count > $downlim) {
         last;
      } 
}
