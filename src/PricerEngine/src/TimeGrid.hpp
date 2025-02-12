#ifndef _TIME_GRID_HPP
#define _TIME_GRID_HPP


#include <nlohmann/json.hpp>
#include <vector>
#include <iostream>

class TimeGrid {



public : 

    std::vector<double> grid_time;
    TimeGrid();
    ~TimeGrid();
    TimeGrid(nlohmann::json json);
    int at(int index);
    int len();
    int getLastIndex(double t);

};



/**
 * return la classe de TimeGrid selon TimeGridType :
 */
extern TimeGrid createTimeGridFromJson(const nlohmann::json json);


#endif 