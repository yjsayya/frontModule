import 'package:flutter/material.dart';

import 'main.dart';
import 'TextField.dart';

void main() {
  runApp(const SecondRoute());
}

class SecondRoute extends StatelessWidget {
  const SecondRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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


      body:Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Container(
            margin: EdgeInsets.all(16.0),
            child: Row(
              children: [
                Expanded(
                  flex: 3,
                  child: TextField(
                    decoration: InputDecoration(
                      labelText: '내용',
                      hintText: '내용을 입력해주세요',
                    ),
                  ),
                ),
                SizedBox(width: 10.0),
                Expanded(
                  flex: 1,
                  child: ElevatedButton(
                    onPressed: () {},
                    child: Text('번역'),
                  ),
                ),
              ],
            ),
          ),
        ],
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
    );
  }
}