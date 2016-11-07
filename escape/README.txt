This is a starter program that doesn't do anything.
To build it you will need a properly setup development environment so
follow the instructions on the Confluence page.

Once your development environment is setup you can run the following
commands and it will build your program.  The first command
builds the Makefile using the cmake program.  If this fails
then you need to get cmake working so let us know what the
errors you see are.  Here is how you run cmake.

   cmake CMakeLists.txt

Once that completes you will find a lot more files in the directory
and now you can build your program by running the "make" command.

   make

At this point you should be able to run the program.

   ./hello

Nothing will happen because this program doesn't do anything
but you shouldn't get any errors...you should just get nothing.

Now you can edit "hello.cpp" and modify the program.  Once you modify
it you can run "make" again.  If you don't have any errors then you
can run the program and see if it works.  Keep doing that until
it does what you want.

When your program does the right thing it will look like this:

   ./hello
   Hello SciBorg!

so...get your program to do that and you can move on to the next one
