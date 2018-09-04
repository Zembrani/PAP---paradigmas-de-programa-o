/*
1) Deve existir uma classe base para o veículo, que defina os dados comuns entre os veículos: cor, placa, modelo, marca,
  ano de fabricação, tipo de veículo, nome do condutor atual.

1.a) Os tipos possíveis de veículos são: moto e carro.
1.b) Entre os atributos, o que deve ser publico, privado ou protegido?
1.c) Deve existir uma função virtual pura que retorne a quantidade de rodas do veículo.

2) Para cada tipo de veículo, deve ser criada uma classe filha que herda a classe base do veículo.
  Em cada uma destas classes, deve ser definido uma função que retorne o número de rodas: uma moto tem duas rodas,
  um carro tem quatro.

3) Uma classe frota deve agrupar os veículos de forma que seja possível encontrar um veículo pela placa em
  um tempo constante. Use um container STL para isso.

4) Crie operações na classe frota: vender, comprar, atribuirMotorista.
*/

#include <iostream>
#include <string>
#include <list>

using namespace std;

class Veiculo {
private:
  string placa;

public:
  string cor, modelo, marca, condutor;
  int ano;
  enum tipoVeiculo {carro, moto};
  Veiculo (void);
  virtual ~Veiculo ();
};

class Carro : public Veiculo  {
private:

public:
  virtual int qtdRodas() {
    return 4;
  }
  Carro (void);
  virtual ~Carro ();
};

class Moto : public Veiculo {
private:

public:
  virtual int qtdRodas() {
    return 2;
  }
  Moto (void);
  virtual ~Moto ();
};

class Frota {
private:

public:
  // void agrupaFrota(list<Veiculo*> *frota);
  string find(list<Veiculo*> *frota, string placaSolicitada);

  void agrupaFrota(list<Veiculo*> *frota){
    // colocar singleton
  }
  Frota ();
  virtual ~Frota ();
};
int main() {
  list<Veiculo*> frota;

}
