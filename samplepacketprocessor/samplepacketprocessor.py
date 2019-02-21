import grpc
import EventNotificationProto_pb2
import ServicesProto_pb2_grpc
import threading
from ryu.lib.packet import packet
import array

# A Simple packet processor.
def packetprocessor():

     channel = grpc.insecure_channel('localhost:50051')
     eventNotificationStub = ServicesProto_pb2_grpc.EventNotificationStub(channel)

     request = EventNotificationProto_pb2.RegistrationRequest(clientId = "packet_processor_python")
     topic = EventNotificationProto_pb2.Topic(clientId = "packet_processor_python"
                                              , type = 0)

     # Register to PACKET_EVENT
     response = eventNotificationStub.register(request)
     eventObserver = eventNotificationStub.onEvent(topic)

     for event in eventObserver:
          pktContext = event.packetContext
          if pktContext is None:
              return
          inboundPkt = pktContext.inboundPacket
          pkt = packet.Packet(inboundPkt.data)
          for p in pkt:
              if type(p)!= str:
                 if p.protocol_name == "ipv4":
                     print("An IPv4 packet has been received")
     while True:
          continue

if __name__ == '__main__':
     t = threading.Thread(target=packetprocessor)
     t.start()

