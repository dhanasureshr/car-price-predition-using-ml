package com.suresh.dhana.carpricepredictionui;

import androidx.appcompat.app.AppCompatActivity;

import android.view.ContextMenu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.*;


import android.os.Bundle;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener
{
   Spinner Fuel_Type_Petrol;
   Spinner Seller_Type_Individual;
   Spinner Transition_Mannual;

   EditText Year,Present_Price,Kms_Driven,Owner;
   Button predictprice;
   TextView outputview;

	//api link
	String url = "https://dh-model-f.herokuapp.com/predict";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		//===============================================================================
		//===============================================================================
		Fuel_Type_Petrol = findViewById(R.id.fueltype);
        Seller_Type_Individual = findViewById(R.id.sellertype);
        Transition_Mannual = findViewById(R.id.transmissiontype);
        Year = findViewById(R.id.year);
        Present_Price = findViewById(R.id.price);
        Kms_Driven = findViewById(R.id.km);
        Owner = findViewById(R.id.owner);
        predictprice = findViewById(R.id.predict);
        outputview = findViewById(R.id.outputview);

		//--------------------------------------------------------------------------------------
		//------------------------------Drop down menu code----------------------------
		//--------------------------------------------------------------------------------------
		ArrayAdapter<CharSequence> fueladapter = ArrayAdapter.createFromResource(
				this,
				R.array.Fueltype,
				android.R.layout.simple_spinner_item
		);

		ArrayAdapter<CharSequence> selleradapter = ArrayAdapter.createFromResource(
				this,
				R.array.Sellertype,
				android.R.layout.simple_spinner_item
		);

		ArrayAdapter<CharSequence> transmissionadapter = ArrayAdapter.createFromResource(
				this,
				R.array.Transmissiontype,
				android.R.layout.simple_spinner_item
		);


		fueladapter.setDropDownViewResource(android.R.layout.simple_spinner_item);
		selleradapter.setDropDownViewResource(android.R.layout.simple_spinner_item);
		transmissionadapter.setDropDownViewResource(android.R.layout.simple_spinner_item);

		Fuel_Type_Petrol.setAdapter(fueladapter);
		Seller_Type_Individual.setAdapter(selleradapter);
		Transition_Mannual.setAdapter(transmissionadapter);

		Fuel_Type_Petrol.setOnItemSelectedListener(this);
		Seller_Type_Individual.setOnItemSelectedListener(this);
		Transition_Mannual.setOnItemSelectedListener(this);


		//-----------------------------------End of menu code-------------------------------------------------

		//----Button logic----
		predictprice.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View view) {
				// predict price button logic here
             StringRequest stringRequest = new StringRequest(
					 Request.Method.POST,
					 url,
					 new Response.Listener<String>() {
						 @Override
						 public void onResponse(String response) {
							 try {
								JSONObject jsonObject = new JSONObject(response);
								String data = jsonObject.getString("Price");
								outputview.setText(data);
							 } catch (JSONException e) {
								 Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_LONG).show();
							 }
						 }
					 },
					 new Response.ErrorListener() {
						 @Override
						 public void onErrorResponse(VolleyError error) {
							 Toast.makeText(MainActivity.this,error.getMessage(), Toast.LENGTH_SHORT).show();
						 }
					 }){
			 	@Override
				public Map getParams()
				{
					Map params = new HashMap();
					params.put("Year",Year.getText().toString());
					params.put("Present_Price",Present_Price.getText().toString());
					params.put("Kms_Driven",Kms_Driven.getText().toString());
					params.put("Owner",Owner.getText().toString());
					params.put("Fuel_Type_Petrol",Fuel_Type_Petrol.getSelectedItem().toString());
					params.put("Seller_Type_Individual",Seller_Type_Individual.getSelectedItem().toString());
					params.put("Transmission_Mannual",Transition_Mannual.getSelectedItem().toString());

                    return params;
				}
			 };

             RequestQueue queue = Volley.newRequestQueue(MainActivity.this);
             queue.add(stringRequest);

			}
		});


	}

	@Override
	public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
		//Fuel_Type_Petrol.getSelectedItem().toString()


	}

	@Override
	public void onNothingSelected(AdapterView<?> adapterView) {

	}
}