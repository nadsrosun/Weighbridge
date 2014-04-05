from osv import osv, fields
  
class weighbridge_info(osv.osv):
    _name = 'weighbridge.info'
    _description = 'Weighbridge Information'

          
    _columns = {
        'vehicle_no': fields.char('Vehicle No', size=100, required = True, translate = True),
	'purpose': fields.selection((('d','Shipment Delivery'), ('s','Sales')),'Purpose'),
	'gross_weight': fields.float('Gross Weight'),
        'weight_in': fields.float('Weight IN'),
        'time_in': fields.datetime('Time IN'),
        'weight_out': fields.float('Weight OUT'),
        'time_out': fields.datetime('Time OUT', required = False),
    }
    _rec_name = 'vehicle_no'

    _defaults = {
        'gross_weight': lambda *a: 0.0,
        'weight_in': lambda *a: 0.0,
        'weight_out': lambda *a: 0.0
    }
     
weighbridge_info()
 
        
