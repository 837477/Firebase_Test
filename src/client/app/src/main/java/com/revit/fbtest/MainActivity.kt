package com.revit.fbtest

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import java.io.IOException
import com.revit.fbtest.databinding.ActivityMainBinding
import com.google.firebase.messaging.FirebaseMessaging

class MainActivity : AppCompatActivity() {
    private val binding by lazy { ActivityMainBinding.inflate(layoutInflater) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        myToken()

    }
    private fun myToken(){
        //쓰레드 사용
        Thread(Runnable {
            try{
                FirebaseMessaging.getInstance().token.addOnCompleteListener {  task ->
                    if (task.isSuccessful){
                        val token = task.result?:""
                        binding.testToken.setText(token)
                    }
                    else{
                        Log.d("로그","토큰 못불러옴")
                    }

                }
            }catch (e: IOException){
                e.printStackTrace()
            }
        }).start()
    }

}
