#include <iostream>
#include <ostream>
#include <string>

struct mdr {
	int x;
	mdr operator*(mdr &param) {

		mdr tmp;

		tmp.x = this->x * param.x;
		return tmp;
	}
};

std::ostream &operator<<(std::ostream &n, mdr &m) {

	n << m.x << std::endl;
	return n;
}


int main() {

	mdr m1;
	m1.x = 2;

	mdr m2;
	m2.x = 5;

	std::cout << m1 << std::endl;
	std::cout << m2 << std::endl;

	mdr m3 = m1 * m2;
	std::cout << m3 << std::endl;
}
