import 'package:flutter/material.dart';

import 'NextPage.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: FirstPage(),
    );
  }
}

class FirstPage extends StatelessWidget {
  const FirstPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('HURIDGE'),
          centerTitle: true,
          leading: IconButton(
            icon: Icon(Icons.menu),
            onPressed: () {
              // 메뉴 버튼 클릭 시 동작할 코드 작성
            },
          ),
          backgroundColor: Colors.blue,
        ),
        body: Container(
          alignment: Alignment.center,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // 첫 번째 버튼 클릭 시 동작할 코드 작성
                },
                style: ElevatedButton.styleFrom(
                  fixedSize: Size(270, 50),
                ),
                child: Text('음성 --> 수화'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {

                  Navigator.push(context, MaterialPageRoute(builder: (context) => const SecondRoute()),);



                },
                style: ElevatedButton.styleFrom(
                  fixedSize: Size(270, 50),
                ),
                child: Text('텍스트 --> 수화'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // 세 번째 버튼 클릭 시 동작할 코드 작성
                },
                style: ElevatedButton.styleFrom(
                  fixedSize: Size(270, 50),
                ),
                child: Text('QR 번역'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // 네 번째 버튼 클릭 시 동작할 코드 작성
                },
                style: ElevatedButton.styleFrom(
                  fixedSize: Size(270, 50),

                ),
                child: Text('영상 및 사진 인식'),
              ),
            ],
          ),
        ),
        bottomNavigationBar: BottomNavigationBar(

          items: const [
            BottomNavigationBarItem(
              backgroundColor: Colors.blue,
              icon: Icon(Icons.home),
              label: 'Home',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.check_circle),
              label: 'Check',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.search),
              label: 'Search',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.settings),
              label: 'Settings',
            ),
          ],
          currentIndex: 0,
          onTap: (index) {
            if (index == 0) {
              // 홈 버튼 클릭 시 동작할 코드 작성
            } else if (index == 1) {
              // 설정 버튼 클릭 시 동작할 코드 작성
            } else if (index == 2) {
              // 기능3 버튼 클릭 시 동작할 코드 작성
            } else if (index == 3) {
              // 기능4 버튼 클릭 시 동작할 코드 작성
            }
          },
        ),
      ),
    );
  }
}
