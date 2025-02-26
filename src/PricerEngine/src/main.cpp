#include <iostream>
#include "Option.hpp"
#include "pnl/pnl_matrix.h"

int main() {
    Option option;
    
    PnlMat *test_matrix = pnl_mat_create_from_list(6, 5,
        3687,   2553.41, 4579.64,  927.45,  875.91,
        4876.3, 3017.8,  5500.34, 1132.99,  915.75,
        4742.5, 2844.17, 6013.87, 1270.2,   911.8,
        4187.8, 2349.89, 5668.45, 1277.3,   742.99,
        4723.8, 2709.35, 6089.84, 1466.47,  888.51,
        5324.9, 3069.16, 6730.73, 1826.77, 1292.15
    );

    double payoff = option.payOff(test_matrix);
    std::cout << "Payoff: " << payoff << std::endl;

    pnl_mat_free(&test_matrix);
    return 0;
}
