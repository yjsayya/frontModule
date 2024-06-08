import 'package:flutter/material.dart';

class MyTextField extends StatefulWidget {
  const MyTextField({Key? key}) : super(key: key);

  @override
  // ignore: library_private_types_in_public_api
  _MyTextFieldState createState() => _MyTextFieldState();
}

class _MyTextFieldState extends State<MyTextField> {
  final _textFieldController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _textFieldController,
      decoration: InputDecoration(
        labelText: '이름',
        hintText: '이름을 입력해주세요',
      ),
    );
  }

  @override
  void dispose() {
    _textFieldController.dispose();
    super.dispose();
  }
}