// Demo of vector plot.
// Compile it with:
//   g++ -o example-vector example-vector.cc -lboost_iostreams -lboost_system 
//   -lboost_filesystem

#include <vector>
#include <cmath>
#include <boost/tuple/tuple.hpp>

#include "gnuplot-iostream.h"

int main() {
	Gnuplot gp;
	// Create a script which can be manually fed into gnuplot later:
	//    Gnuplot gp(">script.gp");
	// Create script and also feed to gnuplot:
	//    Gnuplot gp("tee plot.gp | gnuplot -persist");
	// Or choose any of those options at runtime by setting the
	// GNUPLOT_IOSTREAM_CMD environment variable.

	// Plot four functions: sin(x), cos(x), -sin(x), -cos(x)
	std::vector<boost::tuple<unsigned long, double, double, double, double>> pts_A;

	for(unsigned long i=0; i < 10; i++)
	{
	    pts_A.push_back(boost::make_tuple(
		i,
		cos(i),
		sin(i),
		-cos(i),
		-sin(i))
	    );
	}

	// Don't forget to put "\n" at the end of each line!
	gp << "set xrange [0:10]\nset yrange [-2:2]\n";
	// '-' means read from stdin.  The send1d() function sends data to gnuplot's stdin.
	//gp << "plot '-' with linepoints ls 1 title 'pts_A'\n";
	gp << "plot '-' with linepoints\n";
	gp.send1d(pts_A);

#ifdef _WIN32
	// For Windows, prompt for a keystroke before the Gnuplot object goes
	// out of scope so that the gnuplot window doesn't get closed.
	std::cout << "Press enter to exit." << std::endl;
	std::cin.get();
#endif
}
