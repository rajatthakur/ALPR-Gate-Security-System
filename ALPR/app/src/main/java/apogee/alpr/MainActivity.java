package apogee.alpr;

import android.content.Intent;
import android.os.AsyncTask;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    private TextView textView;
    private EditText editText;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = (EditText) findViewById(R.id.input_num_plate);
        textView = (TextView) findViewById(R.id.textViewOutput);
        textView.setText("");
    }

    public void entryExitListener(View view) {
        textView.setText("");
        new QueryRequest().execute(editText.getText().toString());
    }
    public class QueryRequest extends AsyncTask<String, Void, String> {

        protected void onPreExecute() {
        }

        protected String doInBackground(String... arg0) {

            try {

                URL url = new URL("http://10.0.2.2:8000/carquery/");
                String nplate = arg0[0];
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");
                conn.setDoOutput(true);
                String postParams = "car_plate="+nplate;
                OutputStream os = conn.getOutputStream();
                os.write(postParams.getBytes());
                os.flush();
                os.close();
                Log.d("posted",postParams);
                int responseCode = conn.getResponseCode();
                Log.d("ResCode",Integer.toString(responseCode));
                if(responseCode == HttpURLConnection.HTTP_BAD_REQUEST){
                    Snackbar.make(findViewById(android.R.id.content), "Connection Failed", Snackbar.LENGTH_LONG).show();
                }
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    BufferedReader ina = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                    StringBuffer stringBuffer = new StringBuffer("");
                    String line = "";
                    while ((line = ina.readLine()) != null) {
                        stringBuffer.append(line);
                    }
                    ina.close();
                    return stringBuffer.toString();
                }else{
                    Snackbar.make(findViewById(android.R.id.content), "Connection Failed", Snackbar.LENGTH_LONG).show();
                }
                return null;
            } catch (Exception e) {
                return new String("Exception: " + e.getMessage());
            }

        }

        @Override
        protected void onPostExecute(String result) {
            JSONArray jsonArray = null;
            if(result==null){
                return;
            }
            try {
                jsonArray = new JSONArray(result);
            } catch (JSONException e) {
                e.printStackTrace();
            }
            if(jsonArray==null){
                return;
            }
            int length = jsonArray.length();
            try {
                for(int i = 0;i < length; i++){
                    JSONObject jsonObject = jsonArray.getJSONObject(i);
                    textView.append("In time : " + jsonObject.getString("inTime").toString() + "\n");
                    textView.append("Out time : " + jsonObject.getString("outTime").toString() + "\n-----------------------------------------------------------------------\n");
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
    }
}
