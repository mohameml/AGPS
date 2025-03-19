#ifndef _TIME_GRID_HPP
#define _TIME_GRID_HPP

#include <vector>
#include <iostream>

class TimeGrid {



public : 

    std::vector<double> grid_time;
    TimeGrid();
    ~TimeGrid();
    TimeGrid(std::vector<double> grid_time); 
    double at(int index);
    int len();
    int getLastIndex(double t);
    bool has(double t) const;

};



#endif 