package twitterprocess;

import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer010;
import org.apache.flink.streaming.util.serialization.AvroRowDeserializationSchema;
import org.apache.flink.types.Row;

import java.util.Properties;

public class TwitterProcess {

    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        Properties properties = new Properties();
        properties.setProperty("boostrap.servers", "localhost:9092");

        AvroRowDeserializationSchema schema = new AvroRowDeserializationSchema(java.avro.Twit.class);


        FlinkKafkaConsumer010<Row> myConsumer = new FlinkKafkaConsumer010<Row>("raw", schema, properties);

        myConsumer.setStartFromEarliest();

        DataStream<Row> stream = env.addSource(myConsumer);

    }
}
