#include<iostream>
#include<vector>

//#include"ordenacao.cpp"

using namespace std;

struct parada {
	double latitude, longitude, carga = 0;

	bool operator<(const parada& l, const parada& r){
		return l.latitude > r.latitude ? true : false;
	}
};

template <class T>
void swap(T& x,T& y)
{
     T temp;
     temp=x;
     x=y;
     y=temp;
}

void ordena(parada &registro){
	//pega o valor do meio e compara com os outros dois;
	if(registro[0]>registro[1]) swap(registro[0], registro[1]);
		if else(registro[1]>registro[2]) {
			swap(registro[1], registro[2]);
			return ;
		}
	if(registro[1]>registro[2]) swap(registro[1], registro[2]);
		if else(registro[0]>registro[1]) {
			swap(registro[0], registro[1]);
			return ;
		}

}
int main(int argc, char const *argv[]) {

	std::vector<parada> registro (3);
	double carga_final = 0;

	for (int i = 0; i < 3; ++i) {
		cout << "digite a latitude, longitude e carga com sinal." << endl;
		cin >> registro[i].latitude >> registro[i].longitude >> registro[i].carga;
		carga_final += registro[i].carga;
	}
	//QuickSort(registro);
	ordena(registro);
	for (int i = 0; i < 3; ++i){

		cout << "latitude = " << registro[i].latitude << "\tlongitude = " << registro[i].longitude << endl;
	}
	cout << "carga final = " << carga_final << endl;

	
	return 0;
}


