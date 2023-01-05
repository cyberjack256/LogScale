#Log Data Set Templates

## Manufacturing:
```log
{date} {time} - {machine_id} - {metric}: {value}
{date} {time} - {machine_id} - Alarm: {alarm_type} - {alarm_message}
{date} {time} - {machine_id} - Event: {event_type} - {event_message}
{date} {time} - {machine_id} - Status: {status_type} - {status_message}
{date} {time} - {machine_id} - {sensor_id} - {metric}: {value}
```


These log lines include placeholder values such as`{machine_id}`, `{metric}`, `{value}`, `{alarm_type}`, `{alarm_message}`, `{event_type}`, `{event_message}`, `{status_type}`, and `{status_message}`, which can be replaced with randomly generated fake data using the Faker module.

For example, you could use the following sample log line to generate fake manufacturing logs:

```log
{date} {time} - {machine_id} - {metric}: {value}
```

And the resulting fake log might look like this:

```log
2022-06-20 14:56:45 - MACHINE-123 - Production rate: 500 units/hour
```

```log
{date} {time} - {device_id} - {metric}: {value}
```

And the resulting fake log might look like this:

```log
2022-06-20 14:56:45 - DEVICE-123 - Temperature: 78
```

You can use a similar process to generate fake logs for the other sample log lines. Make sure to use a regular expression to identify the placeholder values in the log format and replace them with fake data using the Faker module.

```json
{"timestamp": "{date} {time}", "equipment_id": "{equipment_id}", "sensor_id": "{sensor_id}", "sensor_name": "{sensor_name}", "sensor_type": "{sensor_type}", "sensor_value": "{sensor_value}", "sensor_units": "{sensor_units}", "prediction": "{prediction}", "prediction_confidence": "{prediction_confidence}"}
{"timestamp": "{date} {time}", "equipment_id": "{equipment_id}", "equipment_name": "{equipment_name}", "equipment_type": "{equipment_type}", "maintenance_type": "{maintenance_type}", "maintenance_schedule": "{maintenance_schedule}", "maintenance_due": "{maintenance_due}"}
{"timestamp": "{date} {time}", "equipment_id": "{equipment_id}", "failure_mode": "{failure_mode}", "failure_impact": "{failure_impact}", "root_cause": "{root_cause}", "preventative_action": "{preventative_action}", "repair_action": "{repair_action}", "downtime": "{downtime}", "repair_time": "{repair_time}"}
```

## Retail:
```log
{date} {time} - {customer_name} ({customer_id}) - Purchased {product} - {price}
{date} {time} - {employee_name} ({employee_id}) - Processed return for {customer_name} ({customer_id}) - {product} - {price}
{date} {time} - {employee_name} ({employee_id}) - Assisted {customer_name} ({customer_id}) with {inquiry_type}
{date} {time} - System error - {error_message}
{date} {time} - {employee_name} ({employee_id}) - Performed inventory for {product} - {quantity}
```

These log lines include placeholder values such as `{customer_name}`, `{customer_id}`, `{product}`, `{price}`, `{employee_name}`, `{employee_id}`, `{inquiry_type}`, `{error_message}`, and `{quantity}`, which can be replaced with randomly generated fake data using the Faker module.

For example, you could use the following sample log line to generate fake retail company logs:

```log
{date} {time} - {customer_name} ({customer_id}) - Purchased {product} - {price}
```
```json
{"timestamp": "{date} {time}", "store_id": "{store_id}", "order_id": "{order_id}", "customer_name": "{customer_name}", "total_amount": "{total_amount}"}
{"timestamp": "{date} {time}", "store_id": "{store_id}", "employee_name": "{employee_name}", "ip": "{ip}"}
{"timestamp": "{date} {time}", "store_id": "{store_id}", "product_name": "{product_name}", "quantity": "{quantity}", "price": "{price}"}
{"timestamp": "{date} {time}", "store_id": "{store_id}", "customer_name": "{customer_name}", "request_type": "{request_type}", "request_details": "{request_details}"}
{"timestamp": "{date} {time}", "store_id": "{store_id}", "campaign_name": "{campaign_name}", "audience": "{audience}", "results": "{results}"}
```

These log lines include placeholder values such as `{store_id}`, `{order_id}`, `{customer_name}`, `{total_amount}`, `{employee_name}`, `{ip}`, `{product_name}`, `{quantity}`, `{price}`, `{request_type}`, `{request_details}`, `{campaign_name}`, `{audience}`, and `{results}`, which can be replaced with randomly generated fake data using the Faker module.

```json
{"timestamp": "{date} {time}", "product_id": "{product_id}", "product_name": "{product_name}", "category": "{category}", "brand": "{brand}", "price": "{price}", "cost": "{cost}", "demand": "{demand}", "competitor_prices": "{competitor_prices}", "price_elasticity": "{price_elasticity}", "recommended_price": "{recommended_price}"}
{"timestamp": "{date} {time}", "region": "{region}", "product_id": "{product_id}", "product_name": "{product_name}", "category": "{category}", "price": "{price}", "demand": "{demand}", "competitor_prices": "{competitor_prices}", "market_share": "{market_share}", "profitability": "{profitability}"}
{"timestamp": "{date} {time}", "product_id": "{product_id}", "product_name": "{product_name}", "category": "{category}", "price": "{price}", "demand": "{demand}", "sales": "{sales}", "margin": "{margin}", "promotion_type": "{promotion_type}", "promotion_discount": "{promotion_discount}", "promotion_sales_lift": "{promotion_sales_lift}"}
```

These log lines include placeholder values such as `{product_id}`, `{product_name}`, `{category}`, `{price}`, and `{demand}`, which can be replaced with actual values specific to your data set. These log lines can be used to store and analyze data related to product pricing, demand, competitor prices, market share, profitability, and promotions, among other things.


TODO: Add description for apache logs for retail

``` log
176.187.208.148 - - [2022-06-20 14:56:45] "POST /app/main/home HTTP/1.1" 371 -
124.63.53.219 - - [2023-01-07 11:12:23] "GET /app/posts/new HTTP/1.1" 369 -
246.96.108.34 - - [2021-09-03 22:31:55] "DELETE /app/users/1 HTTP/1.1" 318 -
237.148.93.8 - - [2022-03-14 23:40:13] "POST /app/posts HTTP/1.1" 354 -
238.111.47.178 - - [2021-11-12 05:20:31] "PUT /app/posts/1 HTTP/1.1" 362 -
```

## Energy:
```log
{date} {time} - {meter_id} - {metric}: {value}
{date} {time} - {meter_id} - Alarm: {alarm_type} - {alarm_message}
{date} {time} - {meter_id} - Event: {event_type} - {event_message}
{date} {time} - {meter_id} - Status: {status_type} - {status_message}
{date} {time} - {meter_id} - {sensor_id} - {metric}: {value}
```

These log lines include placeholder values such as `{meter_id}`, `{metric}`, `{value}`, `{alarm_type}`, `{alarm_message}`, `{event_type}`, `{event_message}`, `{status_type}`, and `{status_message}`, which can be replaced with randomly generated fake data using the Faker module.

For example, you could use the following sample log line to generate fake energy company logs:
```log
{date} {time} - {meter_id} - {metric}: {value}
```
And the resulting fake log might look like this:
```log
2022-06-20 14:56:45 - METER-123 - Electricity consumption: 200 kW
```

You can use a similar process to generate fake logs for the other sample log lines. Make sure to use a regular expression to identify the placeholder values in the log format and replace them with fake data using the Faker module.


## Healthcare:
```json
{"timestamp": "{date} {time}", "patient_id": "{patient_id}", "patient_name": "{patient_name}", "doctor_name": "{doctor_name}", "hospital_name": "{hospital_name}", "diagnosis": "{diagnosis}", "prescription": "{prescription}"}
{"timestamp": "{date} {time}", "patient_id": "{patient_id}", "patient_name": "{patient_name}", "hospital_name": "{hospital_name}", "admission_date": "{admission_date}", "discharge_date": "{discharge_date}", "discharge_summary": "{discharge_summary}"}
{"timestamp": "{date} {time}", "patient_id": "{patient_id}", "patient_name": "{patient_name}", "doctor_name": "{doctor_name}", "hospital_name": "{hospital_name}", "procedure_name": "{procedure_name}", "procedure_date": "{procedure_date}", "procedure_notes": "{procedure_notes}"}
{"timestamp": "{date} {time}", "patient_id": "{patient_id}", "patient_name": "{patient_name}", "doctor_name": "{doctor_name}", "hospital_name": "{hospital_name}", "test_name": "{test_name}", "test_date": "{test_date}", "test_result": "{test_result}"}
{"timestamp": "{date} {time}", "patient_id": "{patient_id}"}
{"timestamp": "{date} {time}", "claim_id": "{claim_id}", "patient_id": "{patient_id}", "patient_name": "{patient_name}", "provider_name": "{provider_name}", "service_date": "{service_date}", "procedure_code": "{procedure_code}", "diagnosis_code": "{diagnosis_code}", "charge_amount": "{charge_amount}", "fraud_indicator": "{fraud_indicator}"}
{"timestamp": "{date} {time}", "study_id": "{study_id}", "sample_id": "{sample_id}", "gene_id": "{gene_id}", "variant_id": "{variant_id}", "chromosome": "{chromosome}", "position": "{position}", "reference_allele": "{reference_allele}", "alternate_allele": "{alternate_allele}", "quality_score": "{quality_score}", "filter_status": "{filter_status}", "info_field": "{info_field}"}
{"timestamp": "{date} {time}", "study_id": "{study_id}", "sample_id": "{sample_id}", "gene_id": "{gene_id}", "transcript_id": "{transcript_id}", "variant_type": "{variant_type}", "consequence": "{consequence}", "impact": "{impact}", "symbol": "{symbol}", "gene_name": "{gene_name}", "gene_region": "{gene_region}", "hgvsc": "{hgvsc}", "hgvsp": "{hgvsp}"}
```

