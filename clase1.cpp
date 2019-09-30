
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;


class persona{


	private:

		int id;
		string name;

	public:

		persona(int _id, string _name);
		void mostrarpersona();
};


persona::persona(int _id, string _name){



	id=_id;
	name=_name;
}

void persona::mostrarpersona() {


	cout <<id<<"\t"<<name<<endl;
}


class estudiante:public persona{


	private:
		float nota;

	public:

		estudiante( int _id, string _name, float _nota);
		void mostrarestudiante();
};



estudiante::estudiante( int _id, string _name, float _nota):persona( _id, _name) {



	nota=_nota;

}


void estudiante::mostrarestudiante(){


	mostrarpersona();
	cout<<nota<<endl;


}



int main(){

	estudiante p1(4324324,"alan",76.4);
	p1.mostrarestudiante();



	return 0;
}
