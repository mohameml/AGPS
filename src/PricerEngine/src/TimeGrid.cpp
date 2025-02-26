#include "TimeGrid.hpp"
#include <nlohmann/json.hpp>
#include <iostream>



TimeGrid::TimeGrid()
{
}

TimeGrid::~TimeGrid()
{
}

TimeGrid::TimeGrid(std::vector<double> grid_time)
{
    this->grid_time = grid_time;

}


int TimeGrid::at(int index)
{
    if(index >= grid_time.size()) {
        std::cout << "bad index : index must be less then size" << std::endl ;
        std::exit(1);
    }
    return this->grid_time.at(index);
}


int TimeGrid::len()
{
    return grid_time.size();
}



int TimeGrid::getLastIndex(double t)
{
    for (int i = 0; i < grid_time.size(); i++)
    {
        if(std::fabs(grid_time.at(i) - t) < 1E-10) {
            return i;
        }
    }
    
    return grid_time.size() - 1;
}


