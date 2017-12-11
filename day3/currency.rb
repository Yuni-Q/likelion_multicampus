require 'eu_central_bank'

from = 'USD'
to = "KRW"

def exchange(from, to)
	bank = EuCentralBank.new
	bank.update_rates 

	return bank.exchange(100, from, to)	
end	


puts "$1 => #{exchange 'USD', 'KRW'}원"