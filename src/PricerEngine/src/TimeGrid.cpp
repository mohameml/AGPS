#include "TimeGrid.hpp"
#include <iostream>
#include <algorithm>



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
    int last_index = grid_time.size() - 1; // Initialisation à une valeur par défaut

    for (int i = 0; i < grid_time.size(); i++)
    {
        if (grid_time.at(i) < t) {
            last_index = i; // Mettre à jour last_index si la date est inférieure à t
        } else {
            break;
        }
    }

    if (last_index != grid_time.size() - 1) {
        std::cout << "last_index = " << last_index << std::endl;
    } else {
        std::cout << "Aucune date trouvée inférieure à t" << std::endl;
    }

    return last_index; // TODO : est ce qu'on doit retourner l'index ou la valeur ?
}


bool TimeGrid::has(double t) const {
    return std::find(grid_time.begin(), grid_time.end(), t) != grid_time.end();
}
