#include<iostream>
#include<vector>

//#include"ordenacao.cpp"

using namespace std;

class Parada {
	public:
		double latitude, longitude, carga;
	
		bool operator>(const Parada& r){
			return this->latitude > r.latitude ? true : false;
		}
};

// std::swap()

template <class T>
void myswap(T& x,T& y)
{
     T temp;
     temp=x;
     x=y;
     y=temp;
}

int main(int argc, char const *argv[]) {

	std::vector<Parada> registro (3);
	double carga_final = 0;

	for (int i = 0; i < 3; ++i)	{
		cout << "digite a latitude, longitude e carga com sinal." << endl;
		cin >> registro[i].latitude >> registro[i].longitude >> registro[i].carga;
	}
	for (int i = 0; i < registro.size() - 1; ++i)	{ //bubble sort para ordenação
		for (int j = i; j < registro.size(); ++j)	{
			if(registro[i].operator>(registro[i])==false){
				myswap(registro[i], registro[j]);
			}
		}
	}

	for (int i = 0; i < registro.size(); ++i){
		cout << "latitude = " << registro[i].latitude << "\tlongitude = " << registro[i].longitude;
		cout << "\tcarga = " << registro[i].carga << endl;
		carga_final += registro[i].carga;
	}
	cout << "carga final = " << carga_final << endl;

	
	return 0;
}


